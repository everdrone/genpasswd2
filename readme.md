# Password generator

## Installation

```sh
pip3 install genpasswd-everdrone
```

## Usage

```
Usage: genpasswd [options]

Options:
  -h, --help            show this help message and exit
  -c LENGTH, --count=LENGTH
                        the count of the strings between separators
  -l SET_LENGTH, --str-length=SET_LENGTH
                        the length of characters between separators
  -d NUMBERS, --digits=NUMBERS
                        the amount of digits in the password
  -u UPPERCASE, --uppercase=UPPERCASE
                        the amount of uppercase letters in the password
  -s SEPARATOR, --separator=SEPARATOR
                        the separator character
  -n ITERATIONS, --number=ITERATIONS
                        executes the command N times
  -v, --version         print the version number and quit
```

Generate 3 passwords

```
$ genpasswd -n 3
ctwewg-ebvlsl-a0Qqre
gkhspu-4Wmplw-izhcaq
fctbnf-qiggnR-bns5wl
```

Generate a password with 4 sets of 5 characters

```
$ genpasswd -c 4 -l 5
jwvq9-vqejL-yzlmv-egfmb
```

Generate a password with 3 digits and 3 uppercase letters

```
$ genpasswd -d 3 -u 3
ipjsGc-aE5mnm-wd5pM0
```

Generate a password using the underscore separator

```
$ genpasswd -s _
qdtclt_lao3Du_tuvsqu
```
