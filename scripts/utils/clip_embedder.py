"""CLIP embedding extraction using OpenCLIP"""

import torch
import numpy as np
from PIL import Image


class CLIPEmbedder:
    """Wrapper for CLIP ViT-L/14 embeddings"""
    
    def __init__(self, model_name='ViT-L-14', pretrained='openai'):
        self.model_name = model_name
        self.pretrained = pretrained
        self.model = None
        self.preprocess = None
        self.device = None
        
    def _init_model(self):
        """Lazy initialization of CLIP model"""
        if self.model is None:
            import open_clip
            
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"Loading CLIP {self.model_name} on {self.device}...")
            
            self.model, _, self.preprocess = open_clip.create_model_and_transforms(
                self.model_name,
                pretrained=self.pretrained,
                device=self.device
            )
            self.model.eval()
            print(f"✓ CLIP model loaded")
    
    def get_embedding(self, image):
        """
        Get CLIP embedding for image
        
        Args:
            image: PIL.Image or path to image
            
        Returns:
            numpy array: (768,) embedding vector for ViT-L/14
        """
        self._init_model()
        
        # Load image if path
        if isinstance(image, str):
            image = Image.open(image).convert('RGB')
        
        # Preprocess
        image_tensor = self.preprocess(image).unsqueeze(0).to(self.device)
        
        # Get embedding
        with torch.no_grad():
            image_features = self.model.encode_image(image_tensor)
            # Normalize
            image_features = image_features / image_features.norm(dim=-1, keepdim=True)
        
        # Convert to numpy
        embedding = image_features.cpu().numpy().squeeze()
        
        return embedding
    
    def get_combined_embedding(self, face_image, full_image, face_weight=0.7):
        """
        Get combined embedding with face focus
        
        Args:
            face_image: PIL.Image of face crop (or None)
            full_image: PIL.Image of full image
            face_weight: Weight for face embedding (0.0-1.0)
            
        Returns:
            numpy array: Combined embedding
        """
        # Get full image embedding
        full_emb = self.get_embedding(full_image)
        
        if face_image is not None:
            # Get face embedding
            face_emb = self.get_embedding(face_image)
            
            # Combine with weighting
            combined = (face_weight * face_emb) + ((1 - face_weight) * full_emb)
            # Renormalize
            combined = combined / np.linalg.norm(combined)
            return combined
        else:
            # No face, use full image only
            return full_emb
