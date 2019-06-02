# NetBSD pkg_admin audit output formatter

Make sure you have python3.7 installed or you will need to change the shebang line.

## Usage message
```bash
./audit-fmt.py --help 
usage: audit-fmt.py [-h] [--outfile OUTPUT_FILE] [--fmt {json,csv}]

Format output of pkg_admin audit

optional arguments:
  -h, --help            show this help message and exit
  --outfile OUTPUT_FILE
  --fmt {json,csv}
```

This *very* simple script takes the output of `pkg_admin audit` and plucks out certain fields for display. There are options to print the output to the screen (default) or to a file. You can specify an csv output or a JSON output.


### Invocation Examples
```bash
$ pkg_admin audit | audit-fmt.py
```

#### JSON output

```bash
$ pkg_admin audit | audit-fmt.py --fmt=json
```

#### JSON output to file
```bash
$ pkg_admin audit | audit-fmt.py --fmt=json --outfile=myfile.json
```


#### CSV output to file
```bash
$ pkg_admin audit | audit-fmt.py --outfile=myfile.csv
```
