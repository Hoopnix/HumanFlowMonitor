# import torchvision
# from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
# from torchvision.models.detection import FasterRCNN
# from torchvision.models.detection.rpn import AnchorGenerator
# from torchvision import utils
# import torch
# import time
#
#
# def get_model_instance(num_classes):
#     model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
#
#     num_classes = 2
#
#     in_features = model.roi_heads.box_predictor.cls_score.in_features
#
#     model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
#
#     backbone = torchvision.models.mobilenet_v2(pretrained=False).features
#
#     backbone.out_channels = 1280
#
#     anchor_generator = AnchorGenerator(sizes=((32, 64, 128, 256, 512),),
#                                        aspect_ratios=((0.5, 1.0, 2.0),))
#
#     roi_pooler = torchvision.ops.MultiScaleRoIAlign(featmap_names=[0],
#                                                     output_size=7,
#                                                     sampling_ratio=2)
#
#     model = FasterRCNN(backbone,
#                        num_classes=2,
#                        rpn_anchor_generator=anchor_generator,
#                        box_roi_pool=roi_pooler)
#     return model
#
# def main():
#     device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
#
#     num_classes = 2
#     transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
#     dataset = torchvision.datasets.VOCDetection(root='E:/Database/VOC', download=False,
#                                                 image_set='train', transform=transform)
#
#     indices = torch.randperm(len(dataset)).tolist()
#     dataset = torch.utils.data.Subset(dataset, indices[:-50])
#
#     data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=4)
#
#     model = get_model_instance(num_classes)
#
#     model.to(device)
#
#     params = [p for p in model.parameters() if p.requires_grad]
#     optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)
#     lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)
#
#     num_epochs = 10
#
#     for epoch in range(num_epochs):
#         loss = torch.nn.CrossEntropyLoss()
#         train_one_epoch(model, optimizer, loss, data_loader, device, epoch)
#         lr_scheduler.step()
#
#     print("Finished!")
#
#
# def train_one_epoch(model, optimizer, loss, data_loader, device, epoch):
#     st = time.time()
#     for i, data in enumerate(data_loader):
#         inputs, labels = data
#         target = []
#         objects = labels['annotation']['object']
#         if isinstance(objects, dict):
#             objects = [objects]
#
#         for j in range(batch_size):
#             d = []
#             label = []
#             d = [[int(objects[i]['bndbox'][tag][j]) for tag in ('xmin', 'ymin', 'xmax', 'ymax')] for i in
#                  range(len(objects))]
#             [label.append(0) for b in range(len(objects))]
#             target.append({'boxes': torch.tensor(d, device=device), 'labels': torch.tensor(label, device=device)})
#         loss_dict = model(inputs.cuda(), target)
#
#         losses = sum(loss for loss in loss_dict.values())
#         print('Epoch ', epoch, losses, 'time:', time.time() - st)
#
#         optimizer.zero_grad()
#         losses.backward()
#         optimizer.step()
#
#
# if __name__ == '__main__':
#     global batch_size
#     batch_size = 1
#     main()
#
