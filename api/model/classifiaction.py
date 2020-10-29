import torch
import torchvision
import torchvision.transforms as transforms
import os

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
dataReturn = [
    ['plane', 'máy bay', 'Type', 'A flying vehicle with wings and one or more engines', '/pleɪn/', 'https://www.oxfordlearnersdictionaries.com/media/english/uk_pron/p/pla/plane/plane__gb_3.mp3'],
    ['car', 'xe hơi', 'Type', 'Where can I park the car?', '/kɑːr/', 'https://www.oxfordlearnersdictionaries.com/media/english/uk_pron/c/car/car__/car__gb_1.mp3'],
    ['bird', 'con chim', 'Type', 'Birds were singing in the trees.', '/bɜːrd/', 'https://www.oxfordlearnersdictionaries.com/media/english/uk_pron/b/bir/bird_/bird__gb_2.mp3'],
    ['cat', 'con mèo', 'Type', 'I have a cat called Bo.', '/kæt/', 'https://www.oxfordlearnersdictionaries.com/media/english/us_pron/c/cat/cat__/cat__us_1.mp3'],
    ['deer', 'con hưu', 'Type', 'An animal with long legs that eats grass, leaves, etc. and can run fast', '/dir/', 'https://www.oxfordlearnersdictionaries.com/media/english/uk_pron/d/dee/deer_/deer__gb_2.mp3'],
    ['dog', 'con chó', 'Type', 'I took the dog for a walk.', '/dɔːɡ/', 'https://www.oxfordlearnersdictionaries.com/media/english/us_pron/d/dog/dog__/dog__us_1_rr.mp3'],
    ['frog', 'con ếch', 'Type', 'The frog jumped into the pond.', '/frɑːɡ/', 'https://www.oxfordlearnersdictionaries.com/media/english/us_pron/f/fro/frog_/frog__us_2_rr.mp3'],
    ['horse', 'con ngựa', 'Type', 'He mounted his horse and rode off.', '/hɔːrs/', 'https://www.oxfordlearnersdictionaries.com/media/english/us_pron/h/hor/horse/horse__us_1.mp3'],
    ['ship', 'con tàu', 'Type', 'A large boat that carries people or goods by sea', '/ʃɪp/', 'https://www.oxfordlearnersdictionaries.com/media/english/us_pron/s/shi/ship_/ship__us_1.mp3'],
    ['truck', 'xe tải', 'Type', 'A large vehicle for carrying heavy loads by road', '/trʌk/', 'https://www.oxfordlearnersdictionaries.com/media/english/us_pron/t/tru/truck/truck__us_1.mp3']
]

import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

import os

net = Net()

module_dir = os.path.dirname(__file__)
path = os.path.join(module_dir, 'cifar_net.pth')
net.load_state_dict(torch.load(path))

from PIL import Image 
  
# creating image object 
# img = Image.open("C:\\Users\\DAVID-DIEP\\Desktop\\car.jpg") 
# img = img.resize((32,32))

# a = transform(img)
# i3 = torch.reshape(a,(1,3,32,32))
# outputs = net(i3)
# _, predicted = torch.max(outputs, 1)

# print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]
#                               for j in range(1)))


def read_image(img):
    # img = Image.open("C:\\Users\\DAVID-DIEP\\Desktop\\car.jpg") 
    img = img.resize((32,32))
    print(img)
    a = transform(img)
    i3 = torch.reshape(a,(1,3,32,32))
    outputs = net(i3)
    _, predicted = torch.max(outputs, 1)

    objectName = classes[predicted[0]]
    
    for i in dataReturn:
        if objectName == i[0]:
            return i
    
    return None
