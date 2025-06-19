# code
import apache_beam as beam

# Define the pipeline
with beam.Pipeline() as pipeline:
    (
        pipeline
        | "Read Input" >> beam.Create(["Apache Beam is awesome", "Learning Direct Runner"])
        | "Split Words" >> beam.FlatMap(lambda line: line.split(" "))
        | "Convert to Lowercase" >> beam.Map(lambda word: word.lower())
        | "Pair Words with 1" >> beam.Map(lambda word: (word, 1))
        | "Count Words" >> beam.CombinePerKey(sum)
        | "Print Results" >> beam.Map(print)
    )
