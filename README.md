## Splicemod

A toolkit for scoring and modifying exons and their adjacent intronic boundaries.

Author: Daniel Bryan Goodman (dbg@mit.edu)

### Python Dependencies

We use Python 2.7.

Required python packages are in requirements.txt and so can be installed with:

```
pip install -r requirements.txt
```

Note that biopython MUST be version 1.57, which is quite old, as splicemod uses
the deprecated `motif` package. It is recommended that you install the requirements in
a python [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

## Running splicemod

After installing the required data and python packages, Splicemod can be run from the base directory with the command:

	`python src/ensembl.py`

## Data required

* Motif definitions are included in the `data/motifs` dir.

* Ensembl mySQL database access (local or remote, see below)

* Wiggle tracks for conservation. This requires approximately 5.3 Gb. These can be downloaded and indexed with
  an included bash script:

    ```
    source scripts/get_wig.sh
    ```

### Ensembl Database

#### Remote Ensembl Access

Ensembl can be used remotely and the host and port can be set in `src/cfg.py`. The defaults
currently work correctly but a list of up-to-date urls can be found [here](http://useast.ensembl.org/info/data/mysql.html).

#### Local Ensembl Copy

A local copy of the ensembl database can also be used for fast access. These directions are based off of the ENSEMBL guide found here:

`http://useast.ensembl.org/info/docs/webcode/mirror/install/ensembl-data.html`

Download the ENSEMBL sql files for both *core* and * from the Ensembl FTP site and unzip them:

```
mkdir -p /path/to/ensembl_db_dir/core
mkdir -p /path/to/ensembl_db_dir/variation
cd /path/to/ensembl_db_dir/core
wget -r ftp://ftp.ensembl.org/pub/release-78/mysql/homo_sapiens_core_78_38/
cd /path/to/ensembl_db_dir/variation
wget -r ftp://ftp.ensembl.org/pub/release-78/mysql/homo_sapiens_variation_78_38/
gunzip *.gz
```

Install mysql if not already installed, and create a DB in the ensembl console:

```
create database homo_sapiens_core_78_38;
```

Then load the schema. I created a user called ensembl and gave it full access to the new db.

```
mkdir -p /path/to/ensembl_db_dir/core
mysql -u ensembl homo_sapiens_core_78_38 < homo_sapiens_core_78_38.sql
mkdir -p /path/to/ensembl_db_dir/variation
```

Then load all the txt data into the new schema. This takes a while.

```
mysqlimport -u ensembl --fields_escaped_by=\\ homo_sapiens_core_78_38 -L *.txt
```

#### Cached Exon List

To speed things up, we cache a copy of all exons in the file `data/ccds_ensembl/78_38_CCDS_exons.all.txt`. This file was generated using the mySQL command in `get_ccds_exons()` function in `ensembl.py` and is hard coded with an exon size of 100. The easiest way to regenerate this file is to run the mySQL query in a program like Sequel Pro and copy the result into a text file, the filename of which is pointed to in `cfg.ens_exon_fn`.

