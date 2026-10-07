import json

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Issue, CriticalIssue, LowPriorityIssue
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

@csrf_exempt
def get_issues(request):

    with open(DATA_DIR / "issues.json", "r", encoding="utf-8") as f:
        issues = json.load(f)

        return JsonResponse(issues, safe=False, status=200)

@csrf_exempt
def get_reporters(request):

    with open(DATA_DIR / "reporters.json", "r", encoding="utf-8") as f:
        reporters = json.load(f)

        return JsonResponse(reporters, safe=False, status=200)

@csrf_exempt
def get_reporter(request):
    reporter_id = request.GET.get("id")

    if not reporter_id:
        return JsonResponse(
            {"error": "id is required"},
            status=400
        )

    try:
        reporter_id = int(reporter_id)
    except ValueError:
        return JsonResponse(
            {"error": "id must be an integer"},
            status=400
        )

    with open(DATA_DIR / "reporters.json", "r", encoding="utf-8") as f:
        reporters = json.load(f)

    for reporter in reporters:
        if reporter["id"] == reporter_id:
            return JsonResponse(reporter, status=200)

    return JsonResponse(
        {"error": "Issue not found"},
        status=404)

@csrf_exempt
def get_issue(request):
    issue_id = request.GET.get("id")

    if not issue_id:
        return JsonResponse(
            {"error": "id is required"},
            status=400
        )

    try:
        issue_id = int(issue_id)
    except ValueError:
        return JsonResponse(
            {"error": "id must be an integer"},
            status=400
        )

    with open(DATA_DIR / "issues.json", "r", encoding="utf-8") as f:
        issues = json.load(f)

    for issue in issues:
        if issue["id"] == issue_id:
            return JsonResponse(issue, status=200)

    return JsonResponse(
        {"error": "Issue not found"},
        status=404)

@csrf_exempt
def create_issue(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST is allowed"},
            status=405
        )


    data = json.loads(request.body)

    try:
        if data["priority"] == "critical":
            issue = CriticalIssue(
            data["id"],
            data["title"],
            data["description"],
            data["status"],
            data["priority"],
            data["reporter_id"],
            data["created_at"]
            )

        elif data["priority"] == "low":
            issue = LowPriorityIssue(
            data["id"],
            data["title"],
            data["description"],
            data["status"],
            data["priority"],
            data["reporter_id"],
            data["created_at"]
            )

        else:
            issue = Issue(
            data["id"],
            data["title"],
            data["description"],
            data["status"],
            data["priority"],
            data["reporter_id"],
            data["created_at"]
        )

        issue.validate()
    except KeyError as e:
        return JsonResponse({"error": str(e)}, status=400)

    response_data = issue.to_dict()
    response_data["message"] = issue.describe()

    return JsonResponse(response_data, status=201)