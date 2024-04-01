# Regex for extraction
REGEX_MATCH_PROXY = r"context = '(?P<proxy>.*)'"
REGEX_MATCH_ENUM = r"enum (?P<name>\w+) {(?P<content>[\w\/=',\n ]+)}"
# sub example: re.sub(REGEX_SUB_COMMENTS[0], REGEX_SUB_COMMENTS[1], input, 0, re.MULTILINE)
# Files
FILES = [
    "out\\originals\\app\\api\\services\\logismata-api-service.ts",
    "out\\originals\\app\\enums\\calculator-enum.ts",
    "out\\originals\\app\\enums\\canton-enum.ts",
    "out\\originals\\app\\enums\\canton-id-enum.ts",
    "out\\originals\\app\\enums\\confession-enum.ts",
    "out\\originals\\app\\enums\\gender-enum.ts",
    "out\\originals\\app\\enums\\language-code-enum.ts",
    "out\\originals\\app\\enums\\path-enum.ts",
    "out\\originals\\app\\enums\\relationship-enum.ts",
    "out\\originals\\app\\enums\\revenue-type-enum.ts",
    "out\\originals\\app\\enums\\tax-budget-main-enum.ts",
    "out\\originals\\app\\enums\\tax-group-id-enum.ts",
    "out\\originals\\app\\enums\\tax-scale-target-enum.ts",
]
