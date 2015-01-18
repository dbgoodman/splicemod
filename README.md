== Splicemod ==

A toolkit for scoring and modifying exons and their adjacent intronic boundaries.

Author: Daniel Bryan Goodman (dbg@mit.edu)

=== Python Dependencies ===

We use Python 2.7.

* pyinterval
* crlibm (for pyinterval)
* Biopython
* bx-python
* acora
* blist
* pycogent
* numpy
* mysql-python
* sqlalchemy

== Data required ==

* Motif definitions in the dropbox folder: (intron/sequences/motifs)
* A mySQL database with the ENSEMBL database (see below for setup instructions)

=== Some notes ===

We use the deprecated Bio.motif submodule of Biopython instead of the newer Bio.motifs, so you might need to use an older version of Biopython if this deprecated function gets removed some point in the future.

=== Ensembl Database ===

A local copy of the ensembl database is required for fast access. These directions are based off of the ENSEMBL guide found here:

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



