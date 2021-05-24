import yaml

with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

print(config['x_0'])
print(config['alpha_0'])
