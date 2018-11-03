## First try
add %HOME/.local to setup.py with inc_dirs and lib_dirs </br>
add path to $LD_LIBRARY_PATH </br>

## ssl support
build openssl from source, install to $HOME/.local </br>
uncomment ssl block in /Modules/Setup, and change path </br>
make sure export LD_LIBRARY_PATH=$HOME/.local/lib </br>

## zlib
build zlib from source, install to $HOME/.local </br>
uncomment zlib block in /Modules/Setup </br>

## _sqlite3
build sqlite from source, install to $HOME/.local </br>

## install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py </br>
use local python get-pip.py --prefix=$HOME/.local/ </br>

