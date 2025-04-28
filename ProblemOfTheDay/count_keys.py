def summarize_logs(logs: list[str]) -> dict[str, int]:
    summary = {}
    for log in logs:
        log_type = log.split("]")[0][1:]  # extract between [ and ]
        summary[log_type] = summary.get(log_type, 0) + 1
    return summary

obj = [
    "[INFO] System started",
    "[ERROR] Crash detected",
    "[WARNING] Low battery",
    "[INFO] Connection established"
]

print(summarize_logs(obj))

