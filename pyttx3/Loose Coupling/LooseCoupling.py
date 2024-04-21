class GreetingService:
    def greet(self, name):
        pass


class EnglishGreetingService(GreetingService):
    def greet(self, name):
        print(f"Hello, {name}")


class FrenchGreetingService(GreetingService):
    def greet(self, name):
        print(f"Bonjour, {name}")


class JapaneseGreetingService(GreetingService):
    def greet(self, name):
        print(f"こんにちは, {name}")


class GreetingServiceFactory:
    def get_greeting_service(self, language):
        if language == "english":
            return EnglishGreetingService()
        elif language == "french":
            return FrenchGreetingService()
        elif language == "japanese":
            return JapaneseGreetingService()
        else:
            raise RuntimeError(f"No greeting service exists for {language} language.")


if __name__ == "__main__":
    lang = input("Enter language (Available languages are french, english, japanese) then name:\n")
    lang = lang.lower()
    name = input()

    greeting_service_factory = GreetingServiceFactory()
    greeting_service = greeting_service_factory.get_greeting_service(lang)
    greeting_service.greet(name)
