import torch
from torch.utils import data
from torch.utils.data import DataLoader
import random
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
class CustomDataset(data.Dataset):
    def __init__(self):
        self.lable = [0]*10
        self.testData = [0]*10
        for i in range(0,10):        
            self.testData[i] = random.randint(0,2)
            self.lable[i] = 0
        n=random.randint(0,9)
        self.testData[n]=random.randint(0,2)*20+random.randint(-5,8)
        self.lable[n]=1
    def __getitem__(self, index):
        lable = list(self.lable)
        testData = list(self.testData)

        return testData[index], lable[index]
    def __len__(self):

        return len(self.lable)
    def get_lable(self):
        return self.lable
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1, 16)
        self.conv1=nn.Conv1d(in_channels=1, out_channels=2,kernel_size=3)
        self.fc2 = nn.Linear(28,16)
        self.fc3 = nn.Linear(16, 2)

    def forward(self, x):

        x = F.relu(self.fc1(x))
        x = x.view(10, 1, 16)
        x = self.conv1(x)
        x = x.view(10, 28)
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
# class Model(nn.modules):
#     def __init__(self):
     
#     def forward(self,x):

test_data = CustomDataset()
test_loader = DataLoader(dataset=test_data,batch_size=10,shuffle=True,drop_last=False)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
net = Net().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(20000):
    
    running_loss = 0.0
    for i, data in enumerate(test_loader, 0):
        # 获取输入数据
        inputs, labels = data

        inputs = torch.tensor(inputs,dtype=torch.float,device=device).view(10,1)
        # print(inputs)
        labels = torch.tensor(labels,device=device)
        # 清空梯度缓存
        optimizer.zero_grad()
        
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        # 打印统计信息
        running_loss += loss.item()

        print('[%d, %5d] loss: %.3f' % (epoch + 1, i+1, running_loss / 2000))
        running_loss = 0.0
for j in range(10):
    for i, data in enumerate(test_loader, 0):
            # 获取输入数据
        inputs, labels = data
        inputs = torch.tensor(inputs,dtype=torch.float,device=device).view(10,1)
        print(inputs)
        # print(inputs)
        labels = torch.tensor(labels,device=device)
        outputs = net(inputs)
        print('outputs: ', outputs)
        # 预测结果
        print('predict: ', torch.max(outputs, 1))
        _, predicted = torch.max(outputs, 1)