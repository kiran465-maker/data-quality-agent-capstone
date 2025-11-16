import os, json
def write_report(df_before, df_after, issues, fixes, validation, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    out = {
        'rows_before': len(df_before),
        'rows_after': len(df_after),
        'issues': issues,
        'fixes': fixes,
        'validation': validation
    }
    with open(os.path.join(out_dir, 'report.json'), 'w') as f:
        json.dump(out, f, indent=2)
    df_after.to_csv(os.path.join(out_dir, 'cleaned.csv'), index=False)
    return os.path.join(out_dir, 'report.json')
