def env_to_bool(env_var):
    return env_var.lower() in ['true', 'yes', 'y', 't', '1']


def env_to_list(env_var):
    return env_var.split(',')
