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

- Run (GPU)
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

## Trouble shooting
- ERROR conda.core.link:_execute_actions(330):  An error occurred while installing package 'conda-forge::qt-4.8.7-vc14_7'
```
conda update conda
conda env remove -n carnd-term1
conda env create -f environment.yml
```
