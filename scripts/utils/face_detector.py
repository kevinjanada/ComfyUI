"""Face detection using InsightFace"""

import numpy as np
from PIL import Image


class FaceDetector:
    """Wrapper for InsightFace face detection"""
    
    def __init__(self, det_thresh=0.5, min_face_size=100):
        self.det_thresh = det_thresh
        self.min_face_size = min_face_size
        self.detector = None
        
    def _init_detector(self):
        """Lazy initialization of detector"""
        if self.detector is None:
            import insightface
            from insightface.app import FaceAnalysis
            
            # Initialize with retinaface_r50 detection model
            self.app = FaceAnalysis(name='buffalo_l', root='.insightface')
            self.app.prepare(ctx_id=0, det_thresh=self.det_thresh)
    
    def detect_face(self, image_path):
        """
        Detect face in image
        
        Returns:
            dict with keys:
                - has_face: bool
                - bbox: [x1, y1, x2, y2] or None
                - confidence: float or None
                - face_image: PIL.Image or None (cropped face)
        """
        self._init_detector()
        
        # Load image
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)
        
        # Detect faces
        faces = self.app.get(img_array)
        
        if not faces:
            return {
                'has_face': False,
                'bbox': None,
                'confidence': None,
                'face_image': None
            }
        
        # Select largest face
        largest_face = max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))
        
        bbox = largest_face.bbox.astype(int)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        
        # Check minimum size
        if width < self.min_face_size or height < self.min_face_size:
            return {
                'has_face': False,
                'bbox': None,
                'confidence': None,
                'face_image': None
            }
        
        # Extract face crop
        x1, y1, x2, y2 = bbox
        # Add small margin
        margin = int(min(width, height) * 0.1)
        x1 = max(0, x1 - margin)
        y1 = max(0, y1 - margin)
        x2 = min(img.width, x2 + margin)
        y2 = min(img.height, y2 + margin)
        
        face_crop = img.crop((x1, y1, x2, y2))
        
        return {
            'has_face': True,
            'bbox': [x1, y1, x2, y2],
            'confidence': float(largest_face.det_score),
            'face_image': face_crop
        }
