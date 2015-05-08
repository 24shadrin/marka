#!/usr/bin/perl

require "sfile";

$truedat=$sfile::fullpath;

print $truedat;
print "\n";

$spath="Beward 1001/1/";

$fullpath="'/home/marka/beward/$truedat/Beward 1001/1/'";

print $fullpath;
print "\n";

@flist = glob "$fullpath/*.jpg";
$i=$#flist;
$j=@flist[$i];
print $j;
print "\n";
