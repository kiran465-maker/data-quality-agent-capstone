class ReportingAgent:
    def __init__(self, output_path="data/output/summary.txt"):
        self.output_path = output_path

    def run(self, message="Pipeline completed successfully."):
        with open(self.output_path, "w") as f:
            f.write(message)

        print(f"[ReportingAgent] Summary saved to: {self.output_path}")
