import json
import os

def generate_reports(df, quality_report, validation_report, output_folder="data/output"):

    # Save cleaned CSV
    df.to_csv(os.path.join(output_folder, "cleaned.csv"), index=False)

    # Save validation report
    with open(os.path.join(output_folder, "validation_report.json"), "w") as f:
        json.dump(validation_report, f, indent=4)

    # Save text summary
    with open(os.path.join(output_folder, "summary.txt"), "w") as f:
        f.write("Quality Summary:\n")
        f.write(str(quality_report))
        f.write("\n\nValidation Summary:\n")
        f.write(str(validation_report))
