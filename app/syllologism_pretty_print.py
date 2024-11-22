from app.utils.syllogism_result import SyllogismResult
from string import ascii_lowercase


def pretty(syllogism_list: list[SyllogismResult]) -> str:
    result_strings = []

    for index, syllogism in enumerate(syllogism_list):
        match syllogism:
            case SyllogismResult('axiom' as syllogism_name, _, _, output_term):
                result_strings.append(f'{index}. {syllogism_name}:\t{output_term}')

            case SyllogismResult(
                syllogism_name, input_terms, substitutions, output_term
            ):
                input_terms_desc = ', '.join(
                    f'{i + 1}=[{term.output_term}]'
                    for i, term in enumerate(input_terms)
                )
                substitutions_desc = ' '.join(
                    f"""{i + 1} """
                    f"""{", ".join(f"{key.lower()}: ({str(sub_t).lower()})" for key, sub_t in subs.items())}"""  # noqa: E501
                    for i, subs in enumerate(substitutions)
                    if subs
                )
                substituted_terms_desc = ', '.join(
                    f'{i + 1}=[{syll.output_term.unify(ascii_lowercase).substitute(**subs).unify()}]'  # noqa: E501
                    for i, (syll, subs) in enumerate(
                        zip(input_terms, substitutions)
                    )
                )

                result_strings.append(
                    f"""{index}. {syllogism_name}:\n"""
                    f"""\tполучено {output_term}\n"""
                    f"""\tиз {input_terms_desc}\n"""
                    f"""\tподстановкой во {substitutions_desc}\n"""
                    f"""\t{substituted_terms_desc}"""
                )

    return '\n'.join(result_strings)
