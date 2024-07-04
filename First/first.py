input_file_path = "Start\\log.txt"
template_file_path = "index.html"
output_file_path = "log_summary.html"

error_count = 0
info_count = 0

with open(input_file_path) as file:
    for line in file:
        if line.startswith("ERROR"):
            error_count += 1
        elif line.startswith("INFO"):
            info_count += 1

with open(template_file_path) as template_file:
    template_content = template_file.read()

html_content = template_content.replace("{error_count}", str(error_count))
html_content = html_content.replace("{info_count}", str(info_count))

with open(output_file_path, "w") as output_file:
    output_file.write(html_content)

print(f"HTML report generated: {output_file_path}")

