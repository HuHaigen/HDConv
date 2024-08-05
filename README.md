# [HDConv: Heterogeneous kernel-based dilated convolutions](https://github.com/HuHaigen/HDConv)

> **The Paper Links**: [Neural Networks](https://www.sciencedirect.com/science/article/pii/S0893608024004921?dgcid=author).

## Abstract （摘要）
Dilated convolution has been widely used in various computer vision tasks due to its ability to expand the receptive field while maintaining the resolution of feature maps. However, the critical challenge is the gridding problem caused by the isomorphic structure of the dilated convolution, where the holes filled in the dilated convolution destroy the integrity of the extracted information and cut off the relevance of neighboring pixels. In this work, a novel heterogeneous dilated convolution, called HDConv, is proposed to address this issue by setting independent dilation rates on grouped channels while keeping the general convolution operation. The heterogeneous structure can effectively avoid the gridding problem while introducing multi-scale kernels in the filters. Based on the heterogeneous structure of the proposed HDConv, we also explore the benefit of large receptive fields to feature extraction by comparing different combinations of dilated rates. Finally, a series of experiments are conducted to verify the effectiveness of some computer vision tasks, such as image segmentation and object detection. The results show the proposed HDConv can achieve a competitive performance on ADE20K, Cityscapes, COCO-Stuff10k, COCO, and a medical image dataset UESTC-COVID-19. The proposed module can readily replace conventional convolutions in existing convolutional neural networks (i.e., plug-and-play), and it is promising to further extend dilated convolution to wider scenarios in the field of image segmentation.

**Keywords: Dilated convolution · Image segmentation · Receptive field · Heterogeneous structure**

## Citation（引用）

Please cite our paper if you find the work useful: 

	@article{HU2024106568,
	title = {HDConv: Heterogeneous kernel-based dilated convolutions},
	journal = {Neural Networks},
	volume = {179},
	pages = {106568},
	year = {2024},
	issn = {0893-6080},
	doi = {https://doi.org/10.1016/j.neunet.2024.106568}
	}

**[⬆ back to top](#0-preface)**
