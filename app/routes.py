from flask import Blueprint, request, jsonify
from .models import db, Subscription

routes = Blueprint('routes', __name__)

@routes.route('/subscriptions', methods=['POST'])
def create_subscription():
    data = request.json
    subscription = Subscription(**data)
    db.session.add(subscription)
    db.session.commit()
    return jsonify({"message": "Subscription created successfully"}), 201

@routes.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    subscriptions = Subscription.query.all()
    result = [
        {
            "id": sub.id,
            "name": sub.name,
            "amount": sub.amount,
            "periodicity": sub.periodicity,
            "start_date": sub.start_date,
            "next_billing_date": sub.next_billing_date,
        }
        for sub in subscriptions
    ]
    return jsonify(result)

@routes.route('/subscriptions/<int:id>', methods=['PUT'])
def update_subscription(id):
    data = request.json
    subscription = Subscription.query.get_or_404(id)
    for key, value in data.items():
        setattr(subscription, key, value)
    db.session.commit()
    return jsonify({"message": "Subscription updated successfully"})

@routes.route('/subscriptions/<int:id>', methods=['DELETE'])
def delete_subscription(id):
    subscription = Subscription.query.get_or_404(id)
    db.session.delete(subscription)
    db.session.commit()
    return jsonify({"message": "Subscription deleted successfully"})
