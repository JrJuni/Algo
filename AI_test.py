import torch

print(torch.__version__)

if torch.cuda.is_available():
    print(torch.version.cuda)
else:
    print("CUDA를 사용할 수 없습니다.")