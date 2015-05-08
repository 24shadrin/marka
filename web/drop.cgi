#!/usr/bin/perl

print "Content-Type: text/html\n\n";
print "<html>";
print "<body>";
print "\n";

$url="index.html";


use File::Copy;

require "sfile";
$truedat=$sfile::fullpath;
$d_path="/web/jpg";

#$p="'/home/marka/beward/$truedat/Beward 1001/1/*'";
$p="/web/dir2/*";
#$p=o;

#записываем список файлов источника в массив
@flist = glob $p;
#обнуление счетчика. вычисляем количество элементов в массиве
$i=0;
$x=$#flist+1;
$j=$x-5;

print "<p><a href=$url> <--back</a></p>";
print "\n";
print $p;
    while ($j<$x) {
#@mas=split("/",@flist[$j]);
#$str=@mas[7];
#print @flist[$j];
#copy ("@flist[$j]","$d_path/$str" || die "Error $!");
print @flist[$j];
#print "\n";
##print $str;
#print "\n";

print "<img src=@flist[$j] width=20%>";
$j++;
#print "\n";
}
print "<p><a href=$url> <--back</a></p>";

print "\n";