#Object detection algorithms.
from PIL import Image
import torch
from torchvision import models, transforms

# Load a pre-trained model for object detection
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Define the image transformations
preprocess = transforms.Compose([
    transforms.ToTensor(),
])

def process_image(image_path):
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Preprocess the image
        image_tensor = preprocess(image).unsqueeze(0)
        
        # Perform object detection
        with torch.no_grad():
            predictions = model(image_tensor)
        
        # Process the predictions
        objects = []
        for box, label, score in zip(predictions[0]['boxes'], predictions[0]['labels'], predictions[0]['scores']):
            if score > 0.5:  # Filter out low confidence detections
                objects.append({
                    "box": box.tolist(),
                    "label": label.item(),
                    "score": score.item()
                })
        
        return {"objects": objects}

    except Exception as e:
        raise ValueError(f"Error processing image: {str(e)}")
