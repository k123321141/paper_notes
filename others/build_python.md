## First try
add %HOME/.local to setup.py with inc_dirs and lib_dirs </b>
add path to $LD_LIBRARY_PATH

## ssl support
build openssl from source, install to $HOME/.local
uncomment ssl block in /Modules/Setup, and change path
--opt edit setup.py ssl code block, and add path to inc_dirs with $HOME/.local/include
make -e LD_LIBRARY_PATH=$HOME/.local/lib

## zlib
build zlib from source, install to $HOME/.local
uncomment zlib block in /Modules/Setup
--opt edit setup.py zlib code block, and add path to lib_dirs with $HOME/.local/lib

## _sqlite3
build sqlite from source, install to $HOME/.local

## install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
use local python get-pip.py --prefix=$HOME/.local/

