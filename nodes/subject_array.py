"""
FLUX2_SubjectArray - Collect multiple subjects into an ordered array
"""

from .base import FLUX2BaseNode, FLUX2Types


class FLUX2_SubjectArray(FLUX2BaseNode):
    """
    Collect multiple subject objects into an ordered array.
    Automatically filters out empty slots and maintains order.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "subject_1": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_2": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_3": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_4": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_5": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_6": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_7": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_8": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_9": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_10": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_11": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
                "subject_12": (FLUX2Types.SUBJECT_OBJECT, {
                    "default": None
                }),
            }
        }
    
    RETURN_TYPES = (FLUX2Types.SUBJECT_ARRAY, "INT", "STRING")
    RETURN_NAMES = ("subjects", "subject_count", "summary")
    FUNCTION = "collect_subjects"
    
    CATEGORY = "FLUX2_Prompt_Builder/Subjects"
    
    def collect_subjects(self,
                        subject_1=None,
                        subject_2=None,
                        subject_3=None,
                        subject_4=None,
                        subject_5=None,
                        subject_6=None,
                        subject_7=None,
                        subject_8=None,
                        subject_9=None,
                        subject_10=None,
                        subject_11=None,
                        subject_12=None):
        """
        Collect subject objects into an array.
        
        Args:
            subject_1 through subject_12: Subject objects
        
        Returns:
            Tuple of (subjects_array, count, summary)
        """
        
        # Collect all non-None subjects
        subjects = []
        for subject in [subject_1, subject_2, subject_3, subject_4, 
                       subject_5, subject_6, subject_7, subject_8,
                       subject_9, subject_10, subject_11, subject_12]:
            if subject is not None:
                subjects.append(subject)
        
        # Count subjects
        count = len(subjects)
        
        # Create summary
        if count == 0:
            summary = "No subjects provided"
        else:
            summary_lines = [f"Total subjects: {count}"]
            for i, subject in enumerate(subjects, 1):
                desc = subject.get("description", "No description")
                # Truncate long descriptions
                if len(desc) > 50:
                    desc = desc[:47] + "..."
                summary_lines.append(f"{i}. {desc}")
            summary = "\n".join(summary_lines)
        
        return (subjects, count, summary)
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # Always execute to ensure updates propagate
        return float("nan")


# For display in UI
FLUX2_SubjectArray.DESCRIPTION = """
Collect multiple subject objects into an ordered array.

Connect up to 12 subjects to this node. Empty slots are automatically 
filtered out, and subjects are maintained in order.

Outputs:
- subjects: Array of subject objects for prompt assembly
- subject_count: Number of subjects in array
- summary: Quick overview of all subjects

Use this node to organize multiple subjects before connecting to the 
Prompt Assembler.

Example workflow:
SubjectCreator (mug) → subject_1
SubjectCreator (laptop) → subject_2
SubjectCreator (plant) → subject_3
→ SubjectArray → PromptAssembler
"""


# Alternative version with priority ordering
class FLUX2_SubjectArrayAdvanced(FLUX2BaseNode):
    """
    Advanced subject array with priority-based ordering.
    Subjects can be reordered based on priority values.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "sort_by_priority": ("BOOLEAN", {
                    "default": False
                }),
            },
            "optional": {
                "subject_1": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_1": ("INT", {"default": 1, "min": 1, "max": 10}),
                "subject_2": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_2": ("INT", {"default": 2, "min": 1, "max": 10}),
                "subject_3": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_3": ("INT", {"default": 3, "min": 1, "max": 10}),
                "subject_4": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_4": ("INT", {"default": 4, "min": 1, "max": 10}),
                "subject_5": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_5": ("INT", {"default": 5, "min": 1, "max": 10}),
                "subject_6": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_6": ("INT", {"default": 6, "min": 1, "max": 10}),
                "subject_7": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_7": ("INT", {"default": 7, "min": 1, "max": 10}),
                "subject_8": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_8": ("INT", {"default": 8, "min": 1, "max": 10}),
                "subject_9": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_9": ("INT", {"default": 9, "min": 1, "max": 10}),
                "subject_10": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_10": ("INT", {"default": 10, "min": 1, "max": 10}),
                "subject_11": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_11": ("INT", {"default": 10, "min": 1, "max": 10}),
                "subject_12": (FLUX2Types.SUBJECT_OBJECT, {"default": None}),
                "priority_12": ("INT", {"default": 10, "min": 1, "max": 10}),
            }
        }
    
    RETURN_TYPES = (FLUX2Types.SUBJECT_ARRAY, "INT", "STRING")
    RETURN_NAMES = ("subjects", "subject_count", "summary")
    FUNCTION = "collect_subjects_advanced"
    
    CATEGORY = "FLUX2_Prompt_Builder/Subjects"
    
    def collect_subjects_advanced(self,
                                 sort_by_priority=False,
                                 subject_1=None, priority_1=1,
                                 subject_2=None, priority_2=2,
                                 subject_3=None, priority_3=3,
                                 subject_4=None, priority_4=4,
                                 subject_5=None, priority_5=5,
                                 subject_6=None, priority_6=6,
                                 subject_7=None, priority_7=7,
                                 subject_8=None, priority_8=8,
                                 subject_9=None, priority_9=9,
                                 subject_10=None, priority_10=10,
                                 subject_11=None, priority_11=10,
                                 subject_12=None, priority_12=10):
        """
        Collect subjects with optional priority-based sorting.
        """
        
        # Collect subjects with priorities
        subject_priority_pairs = []
        for subject, priority in [(subject_1, priority_1), (subject_2, priority_2),
                                  (subject_3, priority_3), (subject_4, priority_4),
                                  (subject_5, priority_5), (subject_6, priority_6),
                                  (subject_7, priority_7), (subject_8, priority_8),
                                  (subject_9, priority_9), (subject_10, priority_10),
                                  (subject_11, priority_11), (subject_12, priority_12)]:
            if subject is not None:
                subject_priority_pairs.append((subject, priority))
        
        # Sort by priority if requested
        if sort_by_priority:
            subject_priority_pairs.sort(key=lambda x: x[1])
        
        # Extract just the subjects
        subjects = [s for s, p in subject_priority_pairs]
        count = len(subjects)
        
        # Create summary
        if count == 0:
            summary = "No subjects provided"
        else:
            summary_lines = [f"Total subjects: {count}"]
            if sort_by_priority:
                summary_lines.append("(Sorted by priority)")
            for i, (subject, priority) in enumerate(subject_priority_pairs, 1):
                desc = subject.get("description", "No description")
                if len(desc) > 40:
                    desc = desc[:37] + "..."
                summary_lines.append(f"{i}. [P{priority}] {desc}")
            summary = "\n".join(summary_lines)
        
        return (subjects, count, summary)
