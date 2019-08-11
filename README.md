# SQID-1.0
(a.k.a. Wikidata Class Browser)

This repository contains the code for the [SQID Wikidata Browser](http://tools.wmflabs.org/sqid/).
You can use the application online without installing anything.

## Legacy version

This is the source code for the (currently still deployed) AngularJS version of SQID that is no longer actively developed. Current development has moved to the `master` branch.

## Submitting comments, bug reports, feature requests

Use the [SQID Issues](https://github.com/Wikidata/SQID/issues) page on
github to report issues and to find out if your issue is already known or even being worked on.

## Installation

You do not normally need to install this yourself, since it is a Web application that you can use in your browser. Developers who want to change the code should have a local copy that runs though. This is farily easy:

* Download the files. The Web application is in the src folder, which should be made accessible through your local web server.
* Get some data. You can copy the example json data files from [src/data/exampleData](src/data/exampleData) to [src/data/](src/data) to get started. You can update these files by running the Python scripts under [helpers/python](helpers/python) from this directory, but this will not recreate all statistics. You can also [download most recent updated json files](http://tools.wmflabs.org/sqid/data/.)
* Optionally recreate all statistics. The program to do this is in the branch "sqid-helper" of [Wikidata Toolkit](https://github.com/Wikidata/Wikidata-Toolkit). The main code is in [SchemaUsageAnalyzer.java](https://github.com/Wikidata/Wikidata-Toolkit/blob/sqid-helper/wdtk-client/src/main/java/org/wikidata/wdtk/client/SchemaUsageAnalyzer.java). The code is invoked by using the command-line client (running the client will show a help message that includes this action).

## License

The code in this repository is released under the [Apache 2.0](LICENSE) license. External libraries used may have their own licensing terms.
