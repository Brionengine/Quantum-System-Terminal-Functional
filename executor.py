import subprocess

class CommandExecutor:
    def execute(self, command):
        try:
            result = subprocess.run(
                command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10  # 10-second timeout
            )
            return result.stdout if result.stdout else "Command executed successfully."
        except subprocess.TimeoutExpired:
            return "Command timed out."
        except subprocess.CalledProcessError as e:
            return f"An error occurred:\n{e.stderr}"
