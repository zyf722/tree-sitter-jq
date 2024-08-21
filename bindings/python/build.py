from setuptools import Extension
from setuptools.command.build_ext import build_ext

extensions = [
    Extension(
        "tree_sitter_jq._binding",
        sources=["bindings/python/tree_sitter_jq/binding.c", "src/parser.c"],
        define_macros=[("Py_LIMITED_API", "0x03080000")],
        include_dirs=["src"],
        py_limited_api=True,
    ),
]


class ExtBuilder(build_ext):
    def run(self):
        build_ext.run(self)

    def build_extension(self, ext):
        build_ext.build_extension(self, ext)


def build(setup_kwargs):
    setup_kwargs.update(
        {"ext_modules": extensions, "cmdclass": {"build_ext": ExtBuilder}}
    )
