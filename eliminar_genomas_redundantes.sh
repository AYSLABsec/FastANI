mkdir -p removed
while read genome; do
  fname=$(basename "$genome")
  mv "cds/$fname" removed/ 2>/dev/null || echo "No encontrado: $fname"
done < redundant_genomes.txt
