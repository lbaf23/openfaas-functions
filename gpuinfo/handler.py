import torch

def handle(req):
    res = {
        "is_available": torch.cuda.is_available(),
        "device_name": torch.cuda.get_device_name(),
        "device_count": torch.cuda.device_count(),
        "current_device": torch.cuda.current_device(),
        "max_memory_allocated": torch.cuda.max_memory_allocated(),

    }
    return res
