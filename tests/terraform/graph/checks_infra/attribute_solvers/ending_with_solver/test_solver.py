import os

from tests.terraform.graph.checks_infra.test_base import TestBaseSolver

TEST_DIRNAME = os.path.dirname(os.path.realpath(__file__))


class TestEndingWithSolver(TestBaseSolver):
    def setUp(self):
        self.checks_dir = TEST_DIRNAME
        super(TestEndingWithSolver, self).setUp()

    def test_ami_ending_with(self):
        root_folder = '../../../resources/public_virtual_machines'
        check_id = "AmiEndingWith"
        should_pass = ['aws_instance.with_open_def_security_groups']
        should_fail = ['aws_instance.with_closed_def_security_groups', 'aws_instance.with_open_security_groups', 'aws_instance.with_subnet_public', 'aws_instance.with_subnet_not_public',]
        expected_results = {check_id: {"should_pass": should_pass, "should_fail": should_fail}}

        self.run_test(root_folder=root_folder, expected_results=expected_results, check_id=check_id)

    def test_ami_ending_with_jsonpath(self):
        root_folder = '../../../resources/public_virtual_machines'
        check_id = "AmiEndingWithJsonpath"
        should_pass = ['aws_instance.with_open_def_security_groups']
        should_fail = ['aws_instance.with_closed_def_security_groups', 'aws_instance.with_open_security_groups', 'aws_instance.with_subnet_public', 'aws_instance.with_subnet_not_public',]
        expected_results = {check_id: {"should_pass": should_pass, "should_fail": should_fail}}

        self.run_test(root_folder=root_folder, expected_results=expected_results, check_id=check_id)

    def test_unrendered(self):
        root_folder = '../../../resources/variable_rendering/unrendered'
        check_id = "UnrenderedVar"
        should_pass = ['aws_s3_bucket.pass1', 'aws_s3_bucket.pass2', 'aws_s3_bucket.pass3']
        should_fail = []
        expected_results = {check_id: {"should_pass": should_pass, "should_fail": should_fail}}

        self.run_test(root_folder=root_folder, expected_results=expected_results, check_id=check_id)
