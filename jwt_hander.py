import jwt


class JwtHandler:

    @staticmethod
    def encode_token(id):
        """
            encoding token
        """
        payload = {"user_id": id}
        token_id = jwt.encode(payload, "secret")
        return token_id

    @staticmethod
    def decode_token(token_id):
        """
            decoding token
        """
        payload = jwt.decode(token_id, "secret", algorithms=["HS256"])
        return payload.get('user_id')