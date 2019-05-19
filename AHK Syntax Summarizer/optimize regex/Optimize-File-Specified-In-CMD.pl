#!/usr/local/bin/perl
# https://metacpan.org/pod/Regexp::Assemble

# To master regular expressions, I recommend 
# http://www.RexEgg.com

my $name_of_file = $ARGV[0];
local $/=undef; 
open my $fh, '<', $name_of_file or die $!;
$file_contents=<$fh>; 
close ($fh);

# Split at each |
@parts = split(/\|/, $file_contents); 

use Regexp::Assemble;
my $ra = Regexp::Assemble->new(flags => 'i' );
 
foreach(@parts) { $ra->add( $_ ); }
print "Version #1: Regex::Assemble\n\n";
print $ra->re . "\n\n"; 

# Let's try Regexp::Assemble::Compressed
# https://metacpan.org/pod/Regexp::Assemble::Compressed
use Regexp::Assemble::Compressed;
my $ra = Regexp::Assemble::Compressed->new;
foreach(@parts) { $ra->add( $_ ); }
print "Version #2: Regex::Assemble::Compressed\n\n";
print $ra->re . "\n\n"; 
