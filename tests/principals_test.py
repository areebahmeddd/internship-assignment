from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    # Create an assignment (DRAFT state)
    response = client.post(
        '/student/assignments',
        headers={'X-Principal': '{"student_id": 1, "user_id": 1}'},
        json={
            'content': 'some text'
        }
    )
    assert response.status_code == 200
    assignment_id = response.json['data']['id']

    # Submit the assignment (SUBMITTED state)
    response = client.post(
        '/student/assignments/submit',
        headers={'X-Principal': '{"student_id": 1, "user_id": 1}'},
        json={
            'id': assignment_id,
            'teacher_id': 2
        }
    )
    assert response.status_code == 200
    
    # Grade the assignment (GRADED state)
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': assignment_id,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

# Same as above, but with a different grade
def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/student/assignments',
        headers={'X-Principal': '{"student_id": 1, "user_id": 1}'},
        json={
            'content': 'some text'
        }
    )
    assert response.status_code == 200
    assignment_id = response.json['data']['id']

    response = client.post(
        '/student/assignments/submit',
        headers={'X-Principal': '{"student_id": 1, "user_id": 1}'},
        json={
            'id': assignment_id,
            'teacher_id': 2
        }
    )
    assert response.status_code == 200

    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': assignment_id,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

def test_get_teachers(client, h_principal):
    response = client.get(
        '/principal/teachers',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for teacher in data:
        assert 'id' in teacher
        assert 'user_id' in teacher
        assert 'created_at' in teacher
        assert 'updated_at' in teacher
