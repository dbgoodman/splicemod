rsync -avz --progress \
    rsync://hgdownload.cse.ucsc.edu/goldenPath/hg38/phyloP100way/hg38.100way.phyloP100way/ \
    data/hg38.100way.phyloP100way/

# make an index for the wig files:
ls data/hg38.100way.phyloP100way/*.gz \
    | parallel \
         "gzcat {} \
        | grep -nb fixedStep \
        | perl -ne 's/(\d+):(\d+).*start=(\d+).*/\$1\t\$2\t\$3/ && print' \
        > {.}.idx"