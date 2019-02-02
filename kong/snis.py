from .components import CrudComponent


class Snis(CrudComponent):
    """Kong SNI API component"""

    async def apply_json(self, data):
        """Apply a JSON data object for a service
        """
        if not isinstance(data, list):
            data = [data]
        result = []
        for entry in data:
            name = entry.pop('name')
            if await self.has(name):
                sni = await self.update(name, **entry)
            else:
                sni = await self.create(name=name, **entry)
            result.append(sni.data)
        return result
