from flask import Blueprint, request, jsonify

tasks_bp = Blueprint('tasks_bp', __name__)

@tasks_bp.route('/approve-task', methods=['POST'])
def approve_task_automatically():
    data = request.get_json()
    
    # টাস্কের আইডি এবং মোট টাকার পরিমাণ যাচাই করা
    task_id = data.get('task_id')
    total_amount = data.get('reward')
    
    if not task_id or not total_amount:
        return jsonify({"error": "প্রয়োজনীয় তথ্য পাওয়া যায়নি!"}), 400

    # ১০% প্ল্যাটফর্ম কমিশন এবং ৯০% ওয়ার্কার পেমেন্ট হিসাব করা
    commission = total_amount * 0.10
    worker_payout = total_amount - commission

    # সফল মেসেজ এবং হিসাব রিটার্ন করা
    return jsonify({
        "status": "success",
        "message": f"কাজ সফলভাবে অনুমোদিত হয়েছে! ১০% কমিশন ({commission} টাকা) কেটে নেওয়ার পর ওয়ার্কারের অ্যাকাউন্টে {worker_payout} টাকা জমা করা হয়েছে।",
        "platform_commission": commission,
        "worker_earnings": worker_payout
    }), 200
