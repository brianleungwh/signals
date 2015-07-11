import mock
import unittest
import subprocess
from yak_communication.main import run_main
from tests.utils import captured_stderr, captured_stdout


class MainTestCase(unittest.TestCase):
    def test_run_command(self):
        command = "python -m yak_communication --schema ./tests/files/test_schema.json --generator ios " \
                  "--datamodels ./tests/files/ --projectname YetiProject"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        self.assertEqual(error, "")
        self.assertIn("Finished generating your files!", output)

    def test_run_main(self):
        with captured_stderr() as error, captured_stdout() as out:
            run_main("./tests/files/test_schema.json", "ios", "./tests/files/", None, "YetiProject", False)
            self.assertEqual(error.getvalue(), "")
            self.assertIn("Finished generating your files!", out.getvalue())

    @mock.patch("yak_communication.generators.ios.ios_generator.subprocess")
    def test_run_main_error(self, mock_subprocess):
        mock_subprocess.check_output.return_value = "Xcode.app"
        with captured_stdout() as out:
            run_main("./tests/files/test_schema.json", "ios", "./tests/files/", "./core/data/path", "YetiProject", False)
            self.assertIn("Must quit Xcode before writing to core data", out.getvalue())
