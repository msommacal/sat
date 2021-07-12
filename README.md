# SAT Solver

This project is a simple SAT solver using Davis-Putnam-Logemann-Loveland (DPLL) algorithm. Thus, it determines if a formula is satisfiable or not. However, it does not give a model of the formula. This is why we advise you to use the minisat solver, which is much more efficient. 

![Screenshot](img/screenshot.png?raw=true "Screenshot")

The input must be in conjunctive normal form (CNF). The DIMACS format or a literal version can be used.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purposes.

### Prerequisites

Make sure that python3 and pip3 is installed, then:

```
pip3 install -r requirements.txt
```

### Installing

First you have to clone the git project:

```
git clone https://github.com/msommacal/sat.git
```

Then you can give the right permissions using chmod (optional):

```
chmod +x tools/decoder.py tools/encoder.py sat.py
```

### Usage

To solve a SAT problem in DIMAC format:

```
./sat.py data/sat0.txt
```

A script is available to encode a literal formula in DIMAC format:

```
echo "(a | ~a)" | tools/encoder.py
```

A second script allows to decode a DIMAC format file:

```
tools/decoder.py < data/sat0.py
```

Example files are available in the data folder. 

## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details.
