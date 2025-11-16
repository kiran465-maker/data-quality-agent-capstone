from tools.report_writer import write_report
class ReportingAgent:
    def generate(self, df_before, df_after, issues, fixes, validation, out_dir):
        return write_report(df_before, df_after, issues, fixes, validation, out_dir)
