

* https://github.com/ChijunShen/TelloPythonControl/



## Poetry

```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry --version

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 -y
python3.10 --version

poetry new myproject
poetry env use python3.10

poetry add ultralytics@8.2.55
poetry add djitellopy@1.5 #https://pypi.org/project/djitellopy/
poetry add opencv-python@4.6.0

poetry add pygame@2.0.1
poetry add numpy@1.26.0

poetry env info
```

<!-- 
## Virtualenv

```sh
pip install virtualenv

virtualenv -p /usr/bin/python3.10.14 myenv

``` -->

## With CONDA

```sh
conda create --name myenvdrone python=3.10.14 #conda create --name myenv
conda activate myenvdrone
conda install package_name
#conda deactivate
```


```sh
#conda install conda-forge::ultralytics 
conda install -c conda-forge ultralytics=8.2.55
conda install -c conda-forge djitellopy=1.5 #https://pypi.org/project/djitellopy/
conda install -c conda-forge opencv-python=4.4.0.46
conda install -c conda-forge pygame=2.0.1
conda install -c conda-forge numpy=1.26.0
```