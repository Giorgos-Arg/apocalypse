import sys
from mappings import mappings

def calculate(inputPath, outputPath, encoding):
    with open(inputPath, 'r', encoding=encoding) as input:
        with open(outputPath, 'a', encoding=encoding) as output:
            for line in input:
                word = line.strip()
                values = [mappings[character] for character in word]
                if(sum(values) == 666):
                    output.write(f'{word} {values}\n')
    output.close()
    input.close()

calculate(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'utf-8')