score_quantization = {'Low':0, 'Medium':1, 'High':1}
df['score_text_quant'] =[ score_quantization[score] for score in df['score_text']]