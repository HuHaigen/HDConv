import torch.nn as nn
import torch


# Basical Version
class HDConv(nn.Module):
    '''
        *dilation* indicates the rate of expansion
    '''
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, bias=True, dilation=(1, 2, 3, 5)):
        super(HDConv, self).__init__()
        self.dilation_1 = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size,
                                    padding=padding + (dilation[0] - 1) * (kernel_size - 1) // 2,
                                    groups=4, bias=bias, dilation=dilation[0], stride=stride)

        self.dilation_2 = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size,
                                    padding=padding + (dilation[1] - 1) * (kernel_size - 1) // 2,
                                    groups=4, bias=bias, dilation=dilation[1], stride=stride)

        self.dilation_3 = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size,
                                    padding=padding + (dilation[2] - 1) * (kernel_size - 1) // 2,
                                    groups=4, bias=bias, dilation=dilation[2], stride=stride)

        self.dilation_4 = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size,
                                    padding=padding + (dilation[3] - 1) * (kernel_size - 1) // 2,
                                    groups=4, bias=bias, dilation=dilation[3], stride=stride)

    def forward(self, x):
        feature1_1, feature1_2, feature1_3, feature1_4 = torch.chunk(self.dilation_1(x), 4, dim=1)
        feature2_1, feature2_2, feature2_3, feature2_4 = torch.chunk(self.dilation_2(x), 4, dim=1)
        feature3_1, feature3_2, feature3_3, feature3_4 = torch.chunk(self.dilation_3(x), 4, dim=1)
        feature4_1, feature4_2, feature4_3, feature4_4 = torch.chunk(self.dilation_4(x), 4, dim=1)

        out_1 = feature1_1 + feature2_2 + feature3_3 + feature4_4
        out_2 = feature1_2 + feature2_3 + feature3_4 + feature4_1
        out_3 = feature1_3 + feature2_4 + feature3_1 + feature4_2
        out_4 = feature1_4 + feature2_1 + feature3_2 + feature4_3
        return torch.cat((out_1, out_2, out_3, out_4), dim=1)


# Basical Version with Groups
class HDConv_groups(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0,  groups=1, bias=True, dilation=(1, 2, 3, 5)):
        super(HDConv_groups, self).__init__()
        self.groups = groups
        self.convs = nn.ModuleList()
        for _ in range(self.groups):
            self.convs.append(HDConv(in_channels // self.groups,
                                     out_channels // self.groups,
                                     kernel_size=kernel_size,
                                     stride=stride,
                                     padding=padding,
                                     bias=bias,
                                     dilation=dilation))

    def forward(self, x):
        x_groups = torch.chunk(x, self.groups, dim=1)
        out = self.convs[0](x_groups[0])
        if self.groups > 1:
            for i in range(1, self.groups):
                out = torch.cat((out, self.convs[i](x_groups[i])), dim=1)
        return out


if __name__ == '__main__':

    in_channels, out_channels = 64, 128
    x = torch.randn(1, in_channels, 224, 224)
    conv3 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1)
    het_conv = HDConv(in_channels, out_channels, kernel_size=3, stride=1, padding=1)
    dy_conv = HDConv(in_channels, out_channels, kernel_size=3, stride=2, padding=1)
    y1 = conv3(x)
    y2 = het_conv(x)
    y3 = dy_conv(x)
    print(x.shape, y1.shape, y2.shape, y3.shape)
