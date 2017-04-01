# Env for Windows 10

## Installation
- Download and install [miniconda](https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe)
- Set up:
```
git clone https://github.com/udacity/CarND-Term1-Starter-Kit.git
cd CarND-Term1-Starter-Kit
move meta_windows_patch.yml meta.yml
```

- Run (CPU)
```
conda env create -f environment.yml
```

- Run (GPU) : GPU prerequisites are requred.
```
conda env create -f environment-gpu.yml
```

- Verify
```
conda info --envs
```

- Uninstall
```
conda env remove -n carnd-term1
```

## Using Anaconda
- Run
```
activate carnd-term1
```
- Stop: close the terminal window
```
deactivate carnd-term1
```

## Using jupyter
- Run
```
jupyter notebook 
```

## GPU Prerequisites
- [Visual C++ Compiler 2015](http://landinghub.visualstudio.com/visual-cpp-build-tools)  - Visual C++ 2015 Build Tool 설치
- [CUDA Drivers 8.0](https://developer.nvidia.com/cuda-downloads)  - cuda_8.0.61_win10 설치
- [CUDNN 5.1](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v5.1/prod_20161129/8.0/cudnn-8.0-windows10-x64-v5.1-zip) - 다운 받은 파일을 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0 에 복사


## Trouble shooting
- ERROR conda.core.link:_execute_actions(330):  An error occurred while installing package 'conda-forge::qt-4.8.7-vc14_7'
```
conda update conda
conda env remove -n carnd-term1
conda env create -f environment.yml
```
