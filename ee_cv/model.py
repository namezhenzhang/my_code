import os
import time
import torch.nn as nn
import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image
from matplotlib import pyplot as plt
import torchvision.models as models
from torch.autograd import Variable
import numpy as np

#import environments
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

classer = ['female','male']

def gci_count(filepath):
#遍历filepath下所有文件，包括子目录
  this_count = 0
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)
    #isdir和isfile参数必须跟绝对路径
    if os.path.isdir(fi_d):
      this_count += gci_count(fi_d)
    else:
      this_count+=1
  return this_count

def loadtraindata(path, batch_size=6, shuffle=True, num_workers=2):
    # 路径
    #path = "data/train"
    trainset = torchvision.datasets.ImageFolder(path, transform=transforms.Compose([
        transforms.Resize(
            (224, 224)),
        transforms.ToTensor()])
    )
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)
    return trainloader


def get_model():

    resnet = models.resnet50(pretrained = True)

    num_ftrs = resnet.fc.in_features
    resnet.fc = nn.Linear(num_ftrs, 2)

    return resnet


def test(model,testloader,criterion):
    print('testing')
    with torch.no_grad():
        model.eval()
        total_loss = 0

        accu_num = 0
        num = 0
        for i,data in enumerate(testloader, 0):
            
            inputs, labels = data
            batch_size = inputs.shape[0]
            num += batch_size
            inputs, labels = Variable(inputs.permute(0,1,2,3)).to(device), Variable(labels).to(device)
            outputs = model(inputs.to(device))
            loss = criterion(outputs, labels)
            total_loss += loss/batch_size

            _, idx = outputs.max(1)
            accu_num += (idx==labels).sum()
        return float(accu_num/float(num)),total_loss/(i+1)

def valid(model,validloader,criterion):
    model.eval()
    total_loss = 0
    for i,data in enumerate(validloader, 0):
        print(i,end=' ')
        inputs, labels = data
        batch_size = inputs.shape[0]
        inputs, labels = Variable(inputs).to(device), Variable(labels).to(device)
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        total_loss += loss/batch_size
    return total_loss/(i+1)

def train(model,optimizer,criterion,trainloader,validloader,testloader,epoch=-1,max_epoch=50):
    step = 200
    min_loss_valid = 100
    early_stop = 0
    early_stop_max_epoch = 5
    loss_list = []
    save_model_step = 5
    save_model_path = 'resnet50_arg/epoch{}.pth'
    print('-'*20)
    print("began training...")
    if epoch != -1:
        print("loading model (epoch {})".format(epoch))
        checkpoint = torch.load(save_model_path.format(epoch))
        resnet18.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        epoch = checkpoint['epoch']
        loss = checkpoint['loss']
    
    
    for epoch in range(epoch+1,max_epoch):
        if early_stop == early_stop_max_epoch:
            print("early stop,before epoch[{}]".format(epoch))
            break
        print("epoch:{}".format(epoch))
        average_loss = 0
        
        for i, data in enumerate(trainloader, 0):
            model.train()
            inputs, labels = data
            batch_size = inputs.shape[0]
            inputs, labels = Variable(inputs).to(device), Variable(labels).to(device)

            outputs = model(inputs.to(device))

            loss = criterion(outputs, labels)

            average_loss+=loss/batch_size
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()


            if (i+1)%step == 0:
                print("epoch[{}],batch[{}],loss[{}]".format(epoch,i,average_loss/step))
                loss_list.append(average_loss/step)
                average_loss = 0
        if (i+1)%step != 0:
                print("epoch[{}],batch[{}],loss[{}]".format(epoch,i,average_loss/((i+1)%step)))
                loss_list.append(average_loss/((i+1)%step))
                average_loss = 0     
                
        # loss_valid = valid(model,validloader,criterion)
        # print('loss valid[{}]'.format(loss_valid))
        # if loss_valid < min_loss_valid:
        #     min_loss_valid = loss_valid
        #     early_stop = 0
        # else :
        #     early_stop += 1    

        if (epoch+1)%save_model_step==0:
            model_save_path = save_model_path.format(epoch)
            torch.save({
            'epoch': epoch,
            'model_state_dict': resnet18.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss
            }, model_save_path)

    if (epoch+1)%save_model_step!=0:
            model_save_path = save_model_path.format(epoch)
            torch.save({
            'epoch': epoch,
            'model_state_dict': resnet18.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            }, model_save_path)

    
    data_array = np.array(loss_list)
    np.savetxt('loss.csv',data_array,delimiter=',')
    print("finished training.")
    #accu,loss_test = test(model,testloader,criterion)

if __name__ == "__main__":
    print('device: ',device)
    resnet18 = get_model()
    resnet18.to(device)
    path = "dataset/{}"

    print('-'*20)

    train_size = gci_count(path.format('train'))
    print('train size:',train_size)
    trainloader = loadtraindata(path.format('train'),batch_size=8)#.to(device)

    valid_batch_size = gci_count(path.format('valid'))
    print('valid size:',valid_batch_size)
    validloader = loadtraindata(path.format('valid'),batch_size=4)

    test_batch_size = gci_count(path.format('test'))
    print('test size:',test_batch_size)
    testloader = None

    optimizer = torch.optim.SGD(resnet18.parameters(), lr=0.001, momentum=0.9)
    criterion = nn.CrossEntropyLoss()

    train(resnet18,optimizer,criterion,trainloader,validloader,testloader,epoch = -1,max_epoch=10)

    testloader = loadtraindata(path.format('test'),batch_size=int(test_batch_size/1000))
    accu,loss_test = test(resnet18,testloader,criterion)
    print("-"*20)
    print("test accu[{}],test loss[{}]".format(accu,loss_test))

    