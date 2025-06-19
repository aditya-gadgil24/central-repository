# Beam code
import apache_beam as beam

with beam.Pipeline() as pipeline:
    (
        pipeline
        | 'Create' >> beam.Create(['to be or not to be'])
        | 'Split' >> beam.FlatMap(lambda x: x.split())
        | 'PairWithOne' >> beam.Map(lambda word: (word, 1))
        | 'GroupAndSum' >> beam.CombinePerKey(sum)
        | 'Format' >> beam.Map(lambda word_count: str(word_count))
        | 'Print' >> beam.Map(print)
    )


    """This is the logic for a simple beam pipeline for processing and transforming data and printing the result or 
    output to console or write to a file"""