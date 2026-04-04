import yaml
import os


class ConfigReader:

    # getting path of env.yaml file
    @staticmethod
    def read_config():
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "env.yaml"
        )

        # opening and reading yaml file
        with open(config_path, "r") as file:
            return yaml.safe_load(file)